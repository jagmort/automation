var waitForEl = function(selector, callback) {
  console.log(selector);
  console.log(i++);
  if(i > 10 || $(selector).is(':visible')) {
    callback();
  } else {
    setTimeout(function() {
      waitForEl(selector, callback);
    }, 1000);
  }
};

$.fn.xpathEvaluate = function (xpathExpression) {
  $this = this.first();

  xpathResult = this[0].evaluate(xpathExpression, this[0], null, XPathResult.ORDERED_NODE_ITERATOR_TYPE, null);

  result = [];
  while (elem = xpathResult.iterateNext()) {
    result.push(elem);
  }

  $result = jQuery([]).pushStack( result );
  return $result;
}

var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0');
var yyyy = today.getFullYear();

var time = prompt("Отсутствует электроэнергия. Отложить до (HH:MM): ")
var date = dd + '.' + mm + '.' + yyyy + ' ' + time;

$("#group_def_tab-history_form-new_comment").val("Отключение э/э до " + time);
$("#group_def_tab-history_form-add_comment").click();

$("#gi_header-takeTask").click();

$("#signal_form-j_idt973").click();
var selector = "#gp_idle_dlg_form-idle_datetime_input";
var i = 0;
waitForEl(selector, function() {
  $(selector).val(date);
  $("#gp_idle_dlg_form-workDelayBtn").click();
});

var selector = "#group_interaction_info_form-tab_view-wait_for_idle_out";
var i = 0;
waitForEl(selector, function() {
  // idle out is visible
});

var selector = "#gi_header-assignTask";
var i = 0;
waitForEl(selector, function() {
  $(selector).click();
});
$("#reassign_dialog_form-select_worksite_label").click();

$(document).xpathEvaluate("//li[contains(text(), 'отключение э/э')]").click();
$("#reassign_dialog_form-reassign").click();
