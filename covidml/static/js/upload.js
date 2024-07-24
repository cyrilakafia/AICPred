const exampleMoleculeButton = document.querySelector(".upload-section__example-btn")
const moleculeIdInput = document.querySelector("input#molecule_id")
const smilesInput = document.querySelector("input#smiles")
const modelTypeSelectInput = document.querySelector("select#model_type")

const exampleMolecule = {
  moleculeId: "44205240",
  smiles: "CCS(=O)(=O)N1CC(C1)(CC#N)N2C=C(C=N2)C3=C4C=CNC4=NC=N3",
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

formTabs.onChange(tab => {
  const queryParams = new URLSearchParams(window.location.search);
  queryParams.set("tab", tab.id.replace("-tab", ""));
  history.replaceState(null, null, "?"+queryParams.toString());
})
formTabs.init(window.INITIAL_TAB_INDEX)

const outputSection = document.querySelector("#results")
if(outputSection != null){
  window.location.hash = "#results"
}