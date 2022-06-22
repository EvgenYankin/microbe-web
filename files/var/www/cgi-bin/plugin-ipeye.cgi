#!/usr/bin/haserl
<%in _common.cgi %>
<%
plugin="ipeye"
page_title="$t_ipeye_0"
%>
<%in _header.cgi %>
<div class="alert alert-warning"><%= $t_alert_1 %></div>
<% if [ "$(yaml-cli -g .ipeye.enabled)" = "true" ]; then %>
<div class="row row-cols-1 row-cols-xl-2 g-3 mb-3">
<div class="col order-2 order-xl-1">
<div class="card mb-3">
<div class="card-header"><%= $t_ipeye_2 %></div>
<div class="card-body">
<form action="/cgi-bin/plugin-ipeye.cgi" method="post" autocomplete="off">
<%
ipeye_camera_name="$hostname"
field_text "ipeye_login"
field_text "ipeye_password"
field_text "ipeye_password"
field_text "ipeye_camera_name"
field_select "ipeye_rtsp_feed"
%>
<button type="submit" class="btn btn-primary mt-3"><%= $t_ipeye_3 %></button>
</form>
</div>
</div>
</div>

<div class="col order-1 order-xl-2">
<p><img src="/a/logo-ipeye.png" alt="Image: IPEYE logo" title="IPEYE Logo"></p>
<p><a href="https://www.ipeye.ru/" target="_blank">www.ipeye.ru</a></p>
<p><%= $t_ipeye_4 %> <a href="https://www.ipeye.ru/" target="_blank"><%= $t_ipeye_5 %></a></p>
</div>
</div>
<script>
function handleSubmit(event) {
  event.preventDefault();
  alert("<%= $t_ipeye_6 %>");
  // API v1 doc: http://31.131.248.100/v1/
  // API v2 doc: http://api.ipeye.ru/doc
}
function initIpEyeForm() { $("form").addEventListener("submit", handleSubmit); }
window.addEventListener("load", initIpEyeForm);
</script>
<% else %>
<div class="alert alert-danger">
<h4><%= $t_ipeye_7 %></h4>
<p><%= $t_ipeye_8 %></p>
<form action="/cgi-bin/majestic-settings-update.cgi" method="post" autocomplete="off">
<input type="hidden" name="mj_ipeye_enabled" id="mj_ipeye_enabled" value="true" class="form-control">
<input type="hidden" name="mj_go_to" id="mj_go_to" value="/cgi-bin/plugin-ipeye.cgi" class="form-control">
<button type="submit" class="btn btn-warning"><%= $t_ipeye_9 %></button>
</form>
</div>
<% fi %>
<%in p/footer.cgi %>
