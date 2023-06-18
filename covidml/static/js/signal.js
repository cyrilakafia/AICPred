class Signal {
  #value
  #subscribers
  constructor(initialValue){
    this.#value = initialValue
    this.#subscribers = new Set()
  }

  get value(){
    return this.#value
  }

  set value(newValue){
    this.#value = newValue
    this.#notifySubscribers()
  }

  subscribe(subscriber, shouldNotifyImmediately = true){
    this.#subscribers.add(subscriber)
    if(!shouldNotifyImmediately) return
    subscriber()
  }

  unsubscribe(subscriber){
    this.#subscribers.delete(subscriber)
  }

  #notifySubscribers(){
    for(const subscriber of [...this.#subscribers]){
      subscriber()
    }
  }
}