function web_submit() {
    var params = $('#form_web').serialize();

    $.ajax({
        url: '/webupdate',
        type: 'POST',
        async: true,
        data: params,
        // dataType: 'json',
        success: function (data, textStatus) {
            console.log(data);
            if (data.status_code === 200) {
                $("#whole").load("/console")
            } else if (data.status_code === 405) {
                data.filelist.forEach(function (value, index, array) {
                    // $("#modal_body").append("<li>" + value + "</li>");
                    $("#ul_modal").append("<li>" + value + "</li>");
                });
                $('#mymodal').modal('show')
            }
        }
    })
}

$(document).ready(function () {
    $('.webdis').attr("disabled", "disabled");
    $('.soadis').attr("disabled", "disabled");

    $("select").change(function () {
        // protype: project type, web or soa
        var protype = $(".nav-tabs li[class='active'] a[data-toggle='tab']").text().toLowerCase();
        var selectText = $("#" + protype + "_select_app option:selected").val();

        if (selectText) {
            if ($("#" + protype + "_txtarea_after").val()) {
                $("." + protype + "dis").removeAttr("disabled")
            }
            $("#" + protype + "_txtarea_before").removeAttr("disabled");
            $("#" + protype + "_input_app").val(selectText);
            // $("#" + protype + "_input_app").removeAttr("disabled");
            format(protype);
        } else {
            $("." + protype + "dis").attr('disabled', "disabled");
            $("#" + protype + "_input_app").val(selectText);
        }
    });

    // modal close
    $("#mymodal").on('hidden.bs.modal', function () {
        $("#ul_modal").find("li").remove();
    });

    $("#modal_btn").click(function () {
        $("#" + protype + "_input_isupdate").val("1");    //1: 强制升级; 0: 不升级，返回检查文件路径
        web_submit();
    })
});

function parse_web(filelist) {
    filelist = filelist.replace(/\\/g, '/');
    filelist = filelist.replace(/\n(\n)*( )*(\n)*\n/g, '\n');
    filelist = filelist.replace(/\.java/g, '\.class');
    filelist = filelist.replace(/.*?src\/main\/(java|resources)\//g, 'WEB-INF/classes/');
    filelist = filelist.replace(/.*?src\/main\/webapp\//g, '');
    filelist = filelist.replace(/(^com\/|^.*?\/com\/)/gm, 'WEB-INF/classes/com/');
    return filelist
}

function parse_soa() {
    return 'hello';
}

function format(protype) {
    var txtr_before = document.getElementById(protype + '_txtarea_before');
    var txtr_after = document.getElementById(protype + '_txtarea_after');
    var filelist = txtr_before.value;

    var div_after = $("#" + protype + "_div_after");

    if (filelist.length === 0) {
        // alert('no lines');
        $("#" + protype + "_txtarea_after").val('');
        div_after.hide();
        $("." + protype + "last").attr("disabled", "disabled");
        return 11;
    }

    if (protype === 'web') {
        pfilelist = parse_web(filelist);

        app = $('#web_select_app').find("option:selected").val();
        if (app) {
            re_app = new RegExp("^.*?" + app + "/", "gm");
            filelist = pfilelist.replace(re_app, '')
        }

        if (/\.class$/gm.test(filelist)) {
            $("#web_radio_reboot").prop('checked', true)
        } else {
            $("#web_radio_noreboot").prop('checked', true)
        }
    } else if (protype === 'soa') {
        pfilelist = parse_soa();
        app = $('#soa_select_app').find("option:selected").val();
        if (app) {
            re_app = new RegExp("^.*?" + app + "/", "gm");
            filelist = pfilelist.replace(re_app, '')
        }
        if (/\.class$/gm.test(filelist)) {
            $("#soa_radio_reboot").prop('checked', true)
        } else {
            $("#soa_radio_noreboot").prop('checked', true)
        }
    }

    row_num = filelist.split('\n').length;
    if (row_num > 8) {
        row_num = 8
    }

    txtr_after.value = filelist;
    txtr_before.rows = row_num;
    txtr_after.rows = row_num;

    div_after.show();
    // $("#web_div_after").attr("readonly", "readonly");
    $("." + protype + "dis").removeAttr("disabled")
}
