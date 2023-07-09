class TabSystem {
  /** @type {HTMLButtonElement[]} */
  #tabs
  /** @type {HTMLElement[]} */
  #tabPanels
  /** @type {((tab: HTMLButtonElement) => void)[]} */
  #changeListeners
  
  /**
   * 
   * @param {HTMLButtonElement[]} tabs 
   * @param {HTMLElement[]} tabPanels 
   */
  constructor(tabs, tabPanels){
    if(tabs.length !== tabPanels.length) throw new Error(`Tabs and tab panels must be the same length\nTabs: ${tabs.length}\nTab panels: ${tabPanels.length}`)
    this.#tabs = tabs
    this.#tabPanels = tabPanels
    this.#changeListeners = []
  }

  /**
   * 
   * @param {string | number | HTMLButtonElement} initialTab
   * @returns 
   */
  init(initialTab = 0){
    this.#tabs.forEach(t => {
      t.setAttribute("role", "tab")
      t.setAttribute("aria-selected", "false")
      t.setAttribute("tabindex", "-1")
      t.addEventListener("click", this.#handleClick.bind(this))
      t.addEventListener("keydown", this.#handleKeyDown.bind(this))
    })

    this.#tabPanels.forEach(p => {
      p.setAttribute("role", "tabpanel")
      p.setAttribute("data-active", "false")
    })

    this.select(initialTab, false)

    return this
  }

  terminate(){
    // TODO: Remove event listeners
  }

  /**
   * 
   * @param {KeyboardEvent} e 
   */
  #handleKeyDown(e){
    if(e.key === "ArrowRight") {
      this.#selectNextTab(e.target)
      e.preventDefault()
    }
    else if(e.key === "ArrowLeft") {
      this.#selectPreviousTab(e.target)
      e.preventDefault()
    }
  }

  /**
   * 
   * @param {MouseEvent} e 
   */
  #handleClick(e){
    this.#selectTab(e.target)
  }

  /**
   * 
   * @param {string | number | HTMLButtonElement} tab 
   * @param {boolean} shouldFocus
   */
  select(tab, shouldFocus = true){
    if(typeof tab === "number") {
      if(tab < 0 || tab > this.#tabs.length) {
        console.warn(`Invalid tab index "${tab}"`)
        return
      }

      this.#selectTab(this.#tabs[tab], shouldFocus)
    }
    else if(typeof tab === "string") {
      const selectedTab = this.#tabs.find(t => t.id === tab)
      if(selectedTab == null) {
        console.warn(`Invalid tab id "${tab}"`)
        return
      }

      this.#selectTab(selectedTab, shouldFocus)
    }
    else if(tab instanceof HTMLElement) {
      const selectedTab = this.#tabs.find(t => t === tab)
      if(selectedTab == null) {
        console.warn(`Invalid tab element "${tab}"`)
        return
      }

      this.#selectTab(selectedTab, shouldFocus)
    }
    else {
      throw new Error("Invalid tab type")
    }
    
    return this
  }

  /**
   * 
   * @param {(tab: HTMLButtonElement) => void} callback 
   */
  onChange(callback){
    this.#changeListeners.push(callback)
    return this
  }

  #notifyChangeListeners(tab){
    this.#changeListeners.forEach(c => c(tab))
  }

  /**
   * 
   * @param {HTMLButtonElement} tab 
   * @param {boolean} shouldFocus
   */
  #selectTab(tab, shouldFocus = true){
    this.#tabs.forEach(t => {
      const isSelected = t === tab
      t.setAttribute("aria-selected", isSelected.toString())
      t.tabIndex = isSelected ? 0 : -1
    })
    
    if(shouldFocus) tab.focus()

    this.#tabPanels.forEach(p => {
      const isActive = p.id === tab.getAttribute("aria-controls")
      p.setAttribute("data-active", isActive.toString())
    })

    this.#notifyChangeListeners(tab)
  }

  /**
   * 
   * @param {HTMLButtonElement} tab 
   */
  #selectNextTab(tab){
    const nextTab = this.#tabs[this.#tabs.indexOf(tab) + 1] ?? this.#tabs[0]
    this.#selectTab(nextTab)
  }

  /**
   * 
   * @param {HTMLButtonElement} tab 
   */
  #selectPreviousTab(tab){
    const previousTab = this.#tabs[this.#tabs.indexOf(tab) - 1] ?? this.#tabs[this.#tabs.length - 1]
    this.#selectTab(previousTab)
  }
}