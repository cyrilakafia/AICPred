const exampleMoleculeButton = document.querySelector(".upload-section__example-btn")
const moleculeIdInput = document.querySelector("input#molecule_id")
const smilesInput = document.querySelector("input#smiles")
const modelTypeSelectInput = document.querySelector("select#model_type")

const exampleMolecule = {
  moleculeId: "2719",
  smiles: "CCN(CC)CCCC(C)NC1=C2C=CC(=CC2=NC=C1)Cl",
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