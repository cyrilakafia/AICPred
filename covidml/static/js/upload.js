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