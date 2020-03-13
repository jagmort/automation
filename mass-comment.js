$("#gi_header-header_frame").html('<textarea id="sdsaa" name="asd" cols="100" rows="30" autocomplete="false" placeholder="Столбец «Тикет» экспортированного из Инити csv" maxlength="100000" class="ui-inputfield ui-inputtextarea ui-widget ui-state-default ui-corner-all width-75-percents ui-inputtextarea-resizable ui-state-hover" role="textbox" aria-disabled="false" aria-readonly="false" aria-multiline="true" data-autosize-on="true" style="overflow: hidden; overflow-wrap: break-word; height: 100px;"></textarea>');
var comment = prompt("Комментарий в ПРМОН");
setTimeout(function() {
    $("#group_interaction_info_form-tab_view-group_interaction_rule_table_data").find("tr").eq(0).find("td").eq(0).find("span").eq(0).find("a").eq(0).click();
}, 5000);

setTimeout(function() {
    var re = $("#sdsaa").val();
    var tr = re.split("\n");
    var long = new Array();

    for(i=0; i < tr.length - 1; i++) {
        long.push(JSON.parse(tr[i]).link.data)
    }

    function osnova() {
        $("div.ui-widget-overlay").remove();
        var all = $("#doldy").contents();
        all.find("#group_def_tab-history_form-new_comment").val(comment);
        var all = $("#doldy").contents();
        all.find("#group_def_tab-history_form-add_comment").click();
        first++;
        $("#doldy").attr('src', long[first]);
        console.log(first);
    }

    var first = 0;
    $( ".ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-shadow.ui-hidden-container.ui-overlay-visible" ).find("div").eq(1).find("iframe").eq(0).attr('id', "doldy");
    $("#doldy").attr('src', long[first]);
    $('#doldy').on("load", function() {
        osnova();
    });
}, 10000);
