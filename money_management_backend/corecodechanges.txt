########  => new changes

filename - apps/frappe/frappe/core/doctype/user/user.py

line number - 800
--------------------------------------------------
def reset_password(user):
	
	if user=="Administrator":
		frappe.local.response.http_status_code = 404      ##########3
		return 'Not allowed'

	try:
		user = frappe.get_doc("User", user)
		if not user.enabled:
			frappe.local.response.http_status_code = 404    #########
			return 'User is disabled'

		user.validate_reset_password()
		user.reset_password(send_email=True)
		frappe.local.response["message"] ="Password reset instructions have been sent to your email" ##############
		return frappe.msgprint(_("Password reset instructions have been sent to your email "))

	except frappe.DoesNotExistError:
		frappe.clear_messages()
		frappe.local.response.http_status_code = 404      ############3
		return 'User not found'


----------------------------------------------------

filename - apps/frappe/frappe/rate_limiter.py

line number - 105
---------------------------------------------------
def ratelimit_decorator(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        # Do not apply rate limits if method is not opted to check
        if methods != 'ALL' and frappe.request and frappe.request.method and frappe.request.method.upper() not in methods:
            return frappe.call(fun, **frappe.form_dict or kwargs)

        _limit = limit() if callable(limit) else limit

        ip = frappe.local.request_ip if ip_based is True else None

        user_key = frappe.form_dict[key] if key else None

        identity = None

        if key and ip_based:
            identity = ":".join([ip, user_key])

        identity = identity or ip or user_key

        if not identity:
            frappe.throw(_('Either key or IP flag is required.'))

        cache_key = f"rl:{frappe.form_dict.cmd}:{identity}"

        value = frappe.cache().get(cache_key) or 0
        if not value:
            frappe.cache().setex(cache_key, seconds, 0)

        value = frappe.cache().incrby(cache_key, 1)
        if value > _limit:
            frappe.local.response.http_status_code = 429           ################
            frappe.local.response["message"] ="You hit the rate limit because of too many requests. Please try after sometime."           ############
            frappe.throw(_("You hit the rate limit because of too many requests. Please try after sometime."))

        return frappe.call(fun, **frappe.form_dict or kwargs)
    return wrapper
return ratelimit_decorator

--------------------------------------------------------------