# Orgs added
SELECT 
	DATE_FORMAT(o.claimed_at, '%Y-%m-01') AS month_year,
	COUNT(*)
FROM Organizations o
WHERE o.destroyed = 0 AND o.claimed_at IS NOT NULL AND o.claimed_at != '0000-00-00 00:00:00:0000'
GROUP BY DATE_FORMAT(o.claimed_at, '%Y-%m-01');



# ORGS WITH A LEADER (grabbing the first leader join date)
SELECT 
    DATE_FORMAT(a.first_leader_joined, '%Y-%m-01') AS month_year,
    COUNT(*) AS total
FROM (
    SELECT
        uo.organization_id,
        MIN(uo.created_at) AS first_leader_joined
    FROM Users_Organizations uo
    INNER JOIN Organizations o ON uo.organization_id = o._id
    WHERE uo.role = 'leader' AND uo.destroyed = 0 AND o.destroyed = 0
    GROUP BY uo.organization_id
) a
GROUP BY DATE_FORMAT(a.first_leader_joined, '%Y-%m-01');



# Orgs with giving enabled
SET @cumsum := 0;
SELECT
    a.month_year,
    @cumsum := @cumsum + a.total AS total
FROM (
    SELECT 
        CASE WHEN o.claimed_at IS NOT NULL AND o.claimed_at != '0000-00-00 00:00:00' THEN DATE_FORMAT(o.claimed_at, '%Y-%m-01') ELSE DATE_FORMAT(o.created_at, '%Y-%m-01') END AS month_year,
        COUNT(o._id) AS total
    FROM Organizations o
    WHERE is_giving_enabled = 1 AND destroyed = 0 AND o.claimed_at IS NOT NULL
    GROUP BY month_year
    ORDER BY 1
) a;



# ENABLED ORGS IN WHICH GIVING HAS TAKEN PLACE*
SELECT
    a.month_year,
    COUNT(a.organization_id) AS total
FROM (
    SELECT
        gp.organization_id,
        DATE_FORMAT(gp.created_at, '%Y-%m-01') AS month_year
    FROM GivingPayments gp
    INNER JOIN Organizations o ON gp.organization_id = o._id
    WHERE 
        o.is_giving_enabled = 1 
        AND o.destroyed = 0
        AND gp.status = 'paid'
        AND gp.refunded = 0
    GROUP BY gp.organization_id
    ORDER BY 2, 1
) a
GROUP BY a.month_year;


# giving accounts verified
SELECT
	DATE_FORMAT(o.claimed_at, '%Y-%m-01') AS month_year,
	COUNT(DISTINCT ga.organization_id)
FROM GivingAccounts ga
INNER JOIN Organizations o ON ga.organization_id = o._id
WHERE 
    ga.destroyed = 0
    AND o.claimed_at IS NOT NULL AND o.claimed_at != '0000-00-00 00:00:00'
GROUP BY DATE_FORMAT(o.claimed_at, '%Y-%m-01');


# total number of registrations
SELECT 
	DATE_FORMAT(u.created_at, '%Y-%m-01') AS month_year,
	COUNT(*)
FROM Users u
WHERE u.destroyed = 0 AND u.phone IS NOT NULL
GROUP BY DATE_FORMAT(u.created_at, '%Y-%m-01')
ORDER BY 1;



# Total # of Religious Members
SELECT
    DATE_FORMAT(a.created_at, '%Y-%m-01') AS month_year,
    COUNT(*) AS total
FROM (
    SELECT
        uo.user_id,
        u.created_at,
        MIN(o.type_id) AS type_id
    FROM Users_Organizations uo
    INNER JOIN Users u ON uo.user_id = u._id
    INNER JOIN Organizations o ON uo.organization_id = o._id
    WHERE 
        u.phone IS NOT NULL
        AND uo.destroyed = 0
        AND u.destroyed = 0
        AND o.destroyed = 0
        AND u.type = 'basic'
    GROUP BY uo.user_id
    HAVING type_id = 1
) a
GROUP BY DATE_FORMAT(a.created_at, '%Y-%m-01')


# Total # of non-Religious Members
SELECT
    DATE_FORMAT(a.created_at, '%Y-%m-01') AS month_year,
    COUNT(*) AS total
FROM (
    SELECT
        uo.user_id,
        u.created_at,
        MIN(o.type_id) AS type_id
    FROM Users_Organizations uo
    INNER JOIN Users u ON uo.user_id = u._id
    INNER JOIN Organizations o ON uo.organization_id = o._id
    WHERE 
        u.phone IS NOT NULL
        AND uo.destroyed = 0
        AND u.destroyed = 0
        AND o.destroyed = 0
        AND u.type = 'basic'
    GROUP BY uo.user_id
    HAVING type_id > 1
) a
GROUP BY DATE_FORMAT(a.created_at, '%Y-%m-01')




