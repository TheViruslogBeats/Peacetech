import { makeAutoObservable } from "mobx";
import axios from "axios";
let url = "http://e8d8-46-242-15-178.ngrok.io";

interface loginForm {
  login: string;
  password: string;
}

interface animation {
  width: string | number;
  height: string | number;
  opacity: number;
}

class LandingPageState {
  loginModal: boolean = false;
  loginForm: loginForm = {
    login: "",
    password: "",
  };

  animation: animation = {
    width: 0,
    height: 0,
    opacity: 0,
  };

  constructor() {
    makeAutoObservable(this);
  }

  async sendLogin() {
    let response = await axios.post(`${url}/authentication`, {
      ...this.loginForm,
    });
    if (response.status === 200) {
      return true;
    } else {
      return false;
    }
  }

  setLM(data: boolean) {
    this.loginModal = data;
    this.setAnimation(data);
  }

  setAnimation(data: boolean) {
    if (data) {
      this.animation = { width: "100%", height: "100%", opacity: 1 };
    } else {
      this.animation = { width: 0, height: 0, opacity: 0 };
    }
  }

  setLF(variable: string, data: string) {
    switch (variable) {
      case "login":
        this.loginForm.login = data;
        break;
      case "password":
        this.loginForm.password = data;
        break;

      default:
        break;
    }
  }
}

export default new LandingPageState();
