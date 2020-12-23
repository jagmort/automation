if(comment.length > 0) {
    document.getElementById("group_def_tab-history_form-new_comment").value = comment;
    $( "button[id='group_def_tab-history_form-add_comment']" ).click();
}

setTimeout(function() {
    var addr = $('#group_interaction_info_form-tab_view-node_rule_building_out-address_ac_out').text();
    var down = $('#group_interaction_info_form-tab_view-calculate_due_date_form_out').text();
    var plan = $('#group_interaction_info_form-tab_view-estimated_end_date_out').text();
    var num = $( "span[class='heading-accent']" ).text();

    var obj = $(".ui-datatable-selectable").find("td").length / 15;
    if(obj < 2) {
        txt = 'устройство';
    }
    else {
        if((obj % 100) > 4 && (obj % 100) < 21) {
            txt = obj + ' устройств';
        }
        else {
            if((obj % 10) < 2) {
                txt = obj + ' устройство';
            }
            else {
                if((obj % 10) < 5) {
                    txt = obj + ' устройства';
                }
                else {
                    txt = obj + ' устройств';
                }
            }
        }
    }

    var dat = $(".ui-datatable-selectable").find("td").eq(0).html().split(';');
    var host = dat[1];
    var per = $("#group_interaction_info_form-tab_view-group_interaction_rule_table_head").find("tr").eq(2).find("th").eq(10).attr('aria-label');
    var ent = $("#group_interaction_info_form-tab_view-group_interaction_rule_table_head").find("tr").eq(2).find("th").eq(9).attr('aria-label');

    var msg = "Недоступно " + txt + " (" + ent + " юл, " + per + " фл" + ") "+ addr + '; ' + host + ".\nВремя начала аварии: " + down + "\nПланируемое время восст: " + plan + "\n" + num;
    $( "div[class='ui-grid-col-12']" ).html('<button class="copy" id="copyw">Перейти в СМС</button><input class="text" id="gert" value="аааа"  />');
    document.getElementById('gert').value = msg;

    var button = document.querySelector('.copy');
    button.addEventListener('click', function(event) {
        var text = document.querySelector('.text');
        text.select();
        document.execCommand('copy');
        if(typeof openSMS === 'undefined' || openSMS === true) window.open("http://omssis-sms.mts-nn.ru/sms2/");
    });
    document.getElementById('copyw').click();

}, 800);
