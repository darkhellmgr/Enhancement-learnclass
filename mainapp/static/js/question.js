    $('#show_q_list').hide();
<!--for deleting question-->
   $(document).on('click', '#deletequestion', function()
 {
   var r = confirm("Are you sure to delete this question");
   if (r == true) {
     $.ajax({
   type: "GET",
   url: $(this).attr('name'),
   context: this,
   success: function(data, status) {
       $(this).parent().hide();
   }
   });
}});
   <!--for viewing question-->
   $(document).on('click', '#questiondetail',function()
   {
     $.ajax({
   type: "GET",
   url: $(this).attr('name'),
   context: this,
   success: function(data, status) {
   x=$(this).attr('data-target');
   var details="<br><br>";
   delete data['Quiz'];
   delete data['question'];
   delete data['course'];
   delete data['topic'];
   delete data['updated_at'];
   delete data['created_at'];


    for (i in data) {
    details+="<b>"+i+"</b>:"+data[i]+"<br>";
   }
   $(x).html(details);
   }
   });
});
$(document).on('click', '#editform',function()
   {
     $.ajax({
   type: "GET",
   url: $(this).attr('name'),
   context: this,
   success: function(data, status) {
   $('#form1').show();
   $('#add_question').hide();
   qid=$(this).attr('value');
   $('#editheader').html("<h2>Edit your question here</h2>");
   $('#myform').find('#idfield').html("<input type='text' hidden name='questionid' value="+qid+">");
   delete data['Quiz'];


    var thiscourse=data['course'];
    var thistopic=data['topic'];
    $('#whichcourse option').removeAttr('selected');
    $('#whichtopic option').removeAttr('selected');
$('#whichcourse option[value='+thiscourse+']').attr('selected','selected');
$('#whichtopic option[value='+thistopic+']').attr('selected','selected');


   if(data['type']=="mcq"){
        eventFire(document.getElementById('mcq'), 'click');
        var mcqdata=JSON.parse(JSON.stringify(data));
        delete mcqdata['question'];
        delete mcqdata['type'];
        delete mcqdata['course'];
        delete mcqdata['topic'];
        delete mcqdata['updated_at'];
        delete mcqdata['created_at'];
        options=Object.keys(mcqdata).length;
        for(i=2;i<options;i++){
        eventFire(document.getElementById('add_option'), 'click');
        }
        var correct=mcqdata['correctanswer'];
        console.log(mcqdata["correctanswer"]);
        delete mcqdata['correctanswer'];
           for(i in mcqdata){
        $("input[name='"+i+"']").val(mcqdata[i]);
        if(mcqdata[i]==correct)
        {
        $("input[value="+i+"]").prop('checked',true);
        }


        }
       }

   else if(data['type']=="truefalse"){
       eventFire(document.getElementById('truefalse'), 'click');
       if(data['correctanswer']=="true"){
       $("input[value='true']").prop('checked',true);
       }
       else{
       $("input[value='false']").prop('checked',true);
       }
}
    else{
       eventFire(document.getElementById('subjective'), 'click');
       }
      $("textarea[name='question']").val(data['question']);

    $(this).parent().parent().parent().hide();
    $('#show_q_list').show();

   }
   });
});
function eventFire(el, etype){
 if (el.fireEvent) {
   el.fireEvent('on' + etype);
 } else {
   var evObj = document.createEvent('Events');
   evObj.initEvent(etype, true, false);
   el.dispatchEvent(evObj);
 }
}

$(document).on('click', '#show_q_list', function()
 {
 location.reload(true);
 });
