app_name = "pollen_live"
app_title = "Pollen Live"
app_publisher = "Nesscale Solutions Pvt Ltd"
app_description = "Pollen Live Development"
app_email = "info@nesscale.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "pollen_live",
# 		"logo": "/assets/pollen_live/logo.png",
# 		"title": "Pollen Live",
# 		"route": "/pollen_live",
# 		"has_permission": "pollen_live.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pollen_live/css/pollen_live.css"
# app_include_js = "/assets/pollen_live/js/pollen_live.js"

# include js, css files in header of web template
# web_include_css = "/assets/pollen_live/css/pollen_live.css"
# web_include_js = "/assets/pollen_live/js/pollen_live.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "pollen_live/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "pollen_live/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "pollen_live.utils.jinja_methods",
# 	"filters": "pollen_live.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "pollen_live.install.before_install"
# after_install = "pollen_live.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "pollen_live.uninstall.before_uninstall"
# after_uninstall = "pollen_live.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "pollen_live.utils.before_app_install"
# after_app_install = "pollen_live.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "pollen_live.utils.before_app_uninstall"
# after_app_uninstall = "pollen_live.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pollen_live.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pollen_live.tasks.all"
# 	],
# 	"daily": [
# 		"pollen_live.tasks.daily"
# 	],
# 	"hourly": [
# 		"pollen_live.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pollen_live.tasks.weekly"
# 	],
# 	"monthly": [
# 		"pollen_live.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "pollen_live.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pollen_live.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "pollen_live.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["pollen_live.utils.before_request"]
# after_request = ["pollen_live.utils.after_request"]

# Job Events
# ----------
# before_job = ["pollen_live.utils.before_job"]
# after_job = ["pollen_live.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"pollen_live.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

