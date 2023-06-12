const moleculeIdInput = document.querySelector("input[name=\"molecule-id\"]")
const smilesInput = document.querySelector("input[name=\"smiles\"]")
const modelTypeSelectInput = document.querySelector("select[name=\"model-type\"]")

const exampleMolecule = {
  moleculeId: "Mol 2",
  smiles: "Oc1cc2c([nH]c(c3nn(C(C)C)c4ncnc(N)c34)c2)cc1",
  modelType: "SVM"
}

// * Call this function to fill form with example
// * You could set it as the click handler of a button or something
function prefillFormWithExample(){
  prefillForm(exampleMolecule)
}

function prefillForm({ moleculeId, smiles, modelType}){
  moleculeIdInput.value = moleculeId
  smilesInput.value = smiles
  modelTypeSelectInput.value = modelType
}