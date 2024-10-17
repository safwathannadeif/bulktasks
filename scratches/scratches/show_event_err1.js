function displyAlert(type,message)
{
const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
const wrapper = document.createElement('div')
wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('')
  alertPlaceholder.append(wrapper)
}



(function () {
   htmx.on("showerror", (e) => {
   displyAlert(e.detail.rType, e.detail.message)

  })
})()
//  https://getbootstrap.com/docs/5.2/components/alerts/
// https://getbootstrap.com/docs/5.3/components/alerts/