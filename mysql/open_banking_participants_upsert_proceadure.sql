CREATE DEFINER=`marcelo`@`%` PROCEDURE `open_banking_participants_upsert`(
id_organization_var varchar(40),
tx_name_var varchar(100),
tx_status_var varchar(10),
dt_modified_var datetime
)
BEGIN
INSERT INTO safra.open_banking_participants(
id_organization,
tx_name,
tx_status,
dt_modified)
values
(id_organization_var,
tx_name_var,
tx_status_var,
dt_modified_var)

ON DUPLICATE KEY UPDATE
tx_name = tx_name_var,
tx_status = tx_status_var,
dt_modified = dt_modified_var;
END