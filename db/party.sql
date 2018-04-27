SELECT 
pp.name,
pp.lastname,
pp.ssn,
pp.ssn_number,
cs.name as subdivision,
cc.name as country,
du.desc  as addreess-- use left join in case no du available 
FROM party_party as pp
left join country_country cc on cc.id = pp.citizenship
left join country_subdivision cs on cs.id = pp.residence
left join gnuhealth_du du on du.id = pp.du
where pp.id = '31'