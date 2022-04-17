Select date_id, make_name, Count(Distinct lead_id) as unique_leads, Count(Distinct partner_id) as unique_partners
From DailySales
Group By date_id, make_name;