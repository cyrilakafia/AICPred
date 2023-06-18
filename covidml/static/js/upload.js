const uploadForm = document.querySelector("form#upload-form")
const fileForm = document.querySelector("form#file-form")
const exampleMoleculeButton = document.querySelector(".upload-section__example-btn")
const moleculeIdInput = document.querySelector("input#molecule_id")
const smilesInput = document.querySelector("input#smiles")
const modelTypeSelectInput = document.querySelector("select#model_type")
const fileInput = document.querySelector("input#txt_file")
const filePreview = document.querySelector(".upload-section__file-preview")
const dropZone = document.querySelector("[data-dropzone]")
const formSeparator = document.querySelector(".upload-section__form-separator")

const EXAMPLE_MOLECULE = {
  moleculeId: "1983",
  smiles: "CC(=O)NC1=CC=C(C=C1)O",
  modelType: "XGBoost"
}

function prefillForm({ moleculeId, smiles, modelType}){
  moleculeIdInput.value = moleculeId
  smilesInput.value = smiles
  modelTypeSelectInput.value = modelType
}

exampleMoleculeButton.addEventListener("click", () => {
  if(isFileSelected.value) fileForm.reset()
  prefillForm(EXAMPLE_MOLECULE)
})

dropZone.addEventListener("dragenter", (e) => {
  e.preventDefault()
  e.stopPropagation()
  dropZone.dataset.hovered = true
})

dropZone.addEventListener("dragover", (e) => {
  e.preventDefault()
  e.stopPropagation()
  dropZone.dataset.hovered = true
})

dropZone.addEventListener("dragleave", (e) => {
  e.preventDefault()
  e.stopPropagation()
  dropZone.dataset.hovered = false
})

dropZone.addEventListener("drop", (e) => {
  e.preventDefault()
  e.stopPropagation()
  dropZone.dataset.hovered = false

  const file = e.dataTransfer.files.item(0)

  if(!file) return
  if(!file.name.endsWith(".txt")) {
    setTimeout(() => {
      alert("Selected file is not a txt file")
    }, 0)
    return
  }
  
  const dt = new DataTransfer()
  dt.items.add(file)
  fileInput.files = dt.files
  isFileSelected.value = true
  selectedFileName.value = file.name
})

fileForm.addEventListener("reset", () => {
  isFileSelected.value = false
})

const isFileSelected = new Signal(false)
isFileSelected.subscribe(() => {
  fileForm.dataset.hasFile = isFileSelected.value
  uploadForm.dataset.hide = isFileSelected.value
  formSeparator.dataset.hide = isFileSelected.value
})

const selectedFileName = new Signal("")
selectedFileName.subscribe(() => {
  filePreview.querySelector("p").textContent = selectedFileName.value
})