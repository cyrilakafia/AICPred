const faqCardList = document.querySelectorAll("button.faq-section__card")
const faqDialogList = document.querySelectorAll("dialog.faq-section__dialog")

for(const card of faqCardList) {
  card.addEventListener("click", () => {
    const target = document.querySelector(`#${card.dataset.target}`)
  
    if(target !== null) {
      target.showModal()
  
      const closeBtn = target.querySelector("button")
      closeBtn?.addEventListener("click", () => {
        target.close()
      })
    }
  })
}

for(const dialog of faqDialogList) {
  dialog.addEventListener("click", (e) => {
    if(e.target !== dialog) return 
    dialog.close()
  })
}