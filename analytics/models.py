from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CustomerReport(models.Model):
	customer_id = models.CharField(max_length=30)
	customer_name = models.CharField(max_length=1000)
	commodity = models.CharField(max_length=30)
	first_read_date = models.CharField(max_length=30)
	first_read_device = models.CharField(max_length=30)
	active_meters_count = models.CharField(max_length=30)
	inactive_meters_count = models.CharField(max_length=30)
	orphaned_meters_count = models.CharField(max_length=30)

class MasterData(models.Model):
	utility = models.CharField(max_length=1000)
	customer_id = models.CharField(max_length=1000)
	status_for_reporting = models.CharField(max_length=1000)
	integrator = models.CharField(max_length=1000)
	build_product = models.CharField(max_length=1000)
	ps_engagement = models.CharField(max_length=1000)
	transformer = models.CharField(max_length=1000)
	energy_insight = models.CharField(max_length=1000)
	voltage_insight = models.CharField(max_length=1000)
	unbilled_energy = models.CharField(max_length=1000)
	oms = models.CharField(max_length=1000)
	sma = models.CharField(max_length=1000)
	additional_notes = models.CharField(max_length=2400)
	rni_new_or_migration = models.CharField(max_length=1000)
	time_zone = models.CharField(max_length=1000)
	w_end_points = models.CharField(max_length=1000)
	e_end_points = models.CharField(max_length=1000)
	g_end_points = models.CharField(max_length=1000)
	jira_ticket = models.CharField(max_length=1000)
	region = models.CharField(max_length=1000)
	project_code = models.TextField(max_length=1000)
	sensus_order = models.CharField(max_length=1000)
	salesforce_case = models.CharField(max_length=1000)
	order_date = models.CharField(max_length=1000)
	sa_handed_to_integrator = models.CharField(max_length=1000)
	sent_for_invoicing_on = models.CharField(max_length=1000)
	annual_fee_trigger_date = models.CharField(max_length=1000)
	one_time_setup_fee = models.CharField(max_length=1000)
	year1_annual_fee = models.CharField(max_length=1000)
	year2_annual_fee = models.CharField(max_length=1000)
	year3_annual_fee = models.CharField(max_length=1000)
	year4_annual_fee = models.CharField(max_length=1000)
	year5_annual_fee = models.CharField(max_length=1000)
	total_end_points = models.CharField(max_length=1000)
	var = models.CharField(max_length=1000)
	point_of_contact = models.CharField(max_length=1000)
	point_of_contact_emails = models.CharField(max_length=1000)
	salesperson = models.CharField(max_length=1000)
	name_of_billing_vendor = models.CharField(max_length=1000)
	training_fee = models.CharField(max_length=1000)
	training_complete = models.CharField(max_length=1000)
	time_order_to_hand_over = models.CharField(max_length=1000)
	time_handover_to_invoice = models.CharField(max_length=1000)
	time_order_to_invoice = models.CharField(max_length=1000)
	time_since_order = models.CharField(max_length=1000)
	column29 = models.CharField(max_length=1000)
	column30 = models.CharField(max_length=1000)
	column31 = models.CharField(max_length=1000)
	column40 = models.CharField(max_length=1000)
	timezone = models.CharField(max_length=1000)
	poc_email = models.CharField(max_length=1000)
	billing_vendor = models.CharField(max_length=1000)
	sa_handed_over_to_integrator_date = models.CharField(max_length=1000)
	column32 = models.CharField(max_length=1000)
	column37 = models.CharField(max_length=1000)
	column38 = models.CharField(max_length=1000)
	column39 = models.CharField(max_length=1000)
	portal_only = models.CharField(max_length=1000)
	migration_type = models.CharField(max_length=1000)

class PortalUtility(models.Model):
	customer_id = models.CharField(max_length=50)
	customer_name = models.CharField(max_length=1000)
	portal_users_count = models.CharField(max_length=100)
	water = models.CharField(max_length=10)
	gas = models.CharField(max_length=10)
	electric = models.CharField(max_length=10)
	alerts = models.CharField(max_length=10)
	bill = models.CharField(max_length=10)
	dashboard_menu = models.CharField(max_length=10)
	goal = models.CharField(max_length=10)
	goals =models.CharField(max_length=10)
	goal_menu = models.CharField(max_length=10)
	google_maps = models.CharField(max_length=10)
	mactivity = models.CharField(max_length=10)
	meters = models.CharField(max_length=10)
	meters_menu = models.CharField(max_length=10)
	notifications = models.CharField(max_length=10)
	outages = models.CharField(max_length=10)
	outages_menu = models.CharField(max_length=10)
	outdoors = models.CharField(max_length=10)
	peers = models.CharField(max_length=10)
	recipients = models.CharField(max_length=10)
	recipients_menu = models.CharField(max_length=10)
	terms = models.CharField(max_length=10)
	treshold = models.CharField(max_length=10)
	tresholds = models.CharField(max_length=10)
	treshhold_menu = models.CharField(max_length=10)
	units = models.CharField(max_length=10)
	units_menu = models.CharField(max_length=10)
	usage = models.CharField(max_length=10)
	usage_detail = models.CharField(max_length=10)
	usage_forecast_menu = models.CharField(max_length=10)
	user = models.CharField(max_length=10)
	user_menu = models.CharField(max_length=10)
	usg_disclaimer = models.CharField(max_length=10)
	other_groups = models.CharField(max_length=10)
	
class BillingsBacklog(models.Model):
	order_status = models.CharField(max_length=100)
	salesperson = models.CharField(max_length=100)
	date_entered = models.CharField(max_length=100)
	cust_name_bill_to = models.CharField(max_length=100)
	customer_name = models.CharField(max_length=100,null=True,blank=True)
	customer_number_bill_to = models.CharField(max_length=100,null=True,blank=True)
	ship_to_number = models.CharField(max_length=100,null=True,blank=True)
	customer_name_ship_to = models.CharField(max_length=100,null=True,blank=True)
	item_number = models.CharField(max_length=100)
	item_description = models.CharField(max_length=1000)
	order_number = models.CharField(max_length=100)
	order_line_number = models.CharField(max_length=100)
	total_sales = models.CharField(max_length=100)
	quantity = models.CharField(max_length=100)
	unit_sales_price = models.CharField(max_length=100)
	project_code = models.CharField(max_length=100)
	date_invoiced = models.CharField(max_length=100)
	ship_to_number = models.CharField(max_length=100)
	early_ship = models.CharField(max_length=100)
	promotion_region = models.CharField(max_length=100)
	product_code = models.CharField(max_length=100)
	entered_by = models.CharField(max_length=100)
	item_class = models.CharField(max_length=100)
	date_committed = models.CharField(max_length=100)
	customer_no_bill_to = models.CharField(max_length=100,null=True,blank=True)
	date_requested = models.CharField(max_length=100)
	date_customer_request = models.CharField(max_length=100)
	customer_po = models.CharField(max_length=100)
	warehouse = models.CharField(max_length=100)
	facility = models.CharField(max_length=100)
	item_type = models.CharField(max_length=100)
	ship_to_state = models.CharField(max_length=100)
	invoice_number = models.CharField(max_length=100)
	manufacturing_group = models.CharField(max_length=100)
	hold_reason = models.CharField(max_length=100)
	po_number = models.CharField(max_length=100)
	