const exampleMoleculeButton = document.querySelector(".upload-section__example-btn")
const moleculeIdInput = document.querySelector("input#molecule_id")
const smilesInput = document.querySelector("input#smiles")
const modelTypeSelectInput = document.querySelector("select#model_type")

const exampleMolecule = {
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
  prefillForm(exampleMolecule)
})

const formTabs = new TabSystem(
  Array.from(document.querySelectorAll("button[role=tab]")),
  Array.from(document.querySelectorAll("div[role=tabpanel]"))
)

formTabs.init()

const outputSection = document.querySelector("#results")
if(outputSection != null){
  window.location.hash = "#results"
}