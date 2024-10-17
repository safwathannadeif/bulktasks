#https://htmx.org/headers/hx-trigger/
document.body.addEventListener("showerror", function(evt){
    alert(evt.detail.rtype);
})
function displyAlert(type,message)
{

const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
alert("MSGNo 1 getting alertPlaceholder="+alertPlaceholder)

alert( "MSGNO 2 before warp divconst wrapper ... OK Inputs type and message" + " " + type + "  " + message )
  const wrapper = document.createElement('div')

  alert( "MSGNO 3 const wrapper ... OK Inputs type and message" + " " + type + "  " + message )
  wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('')

  alertPlaceholder.append(wrapper)

}




(function () {
//   const myAlert = document.getElementById("alert1")
//
//   const aa = new bootstrap.Alert(myAlert)

   htmx.on("showerror", (e) => {
   alert( "showerr HTMX Event with Messga ************************")
   alert( "showerr HTMX Event with Messga e.detail.message:" + e.detail.message)
   alert( "showerr HTMX Event with the e Messge e.detail,rtype:" + e.detail.rtype)
//   var json = JSON.parse(e)
//   alert("showerror =" +  json("showerror"))
//   alert("rtype =" +  json("rtype"))

   displyAlert(e.detail,rtype:, e.detail.message)


  })
})()

//  https://getbootstrap.com/docs/5.2/components/alerts/
// https://getbootstrap.com/docs/5.3/components/alerts/