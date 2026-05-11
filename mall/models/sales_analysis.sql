-- models/sales_analysis.sql

select
    sales_channel,
    COUNT(*) as total_sales,
    SUM(revenue) as total_revenue,
    AVG(revenue) as average_revenue
from
    {{ ref('sales_data') }}
group by 
    sales_channel
having SUM(revenue) >= 0