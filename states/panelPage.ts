import { makeAutoObservable } from "mobx";

class PanelPageStore {
  notifications: boolean = false;
  constructor() {
    makeAutoObservable(this);
  }

  setNM(data: boolean) {
    this.notifications = data
  }
}

export default new PanelPageStore();
