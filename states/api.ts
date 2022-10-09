import axios from "axios";
import { runInAction, makeAutoObservable } from "mobx";
import { url } from "./url";

const $api = axios.create({
  withCredentials: true,
  baseURL: url,
});

interface userData {
  role: string;
  status: string;
  rating: rating;
  count: number;
  digRub: number;
  tokens: tokens[];
  tasks: tasks[]
}

interface tasks {
  description: string;
  award: number;
  administrator_login: string;
  progress: number;
}

interface tokens {
  uri: string;
  tokens: number[];
}

interface rating {
  place: number;
  score: number;
}

class Api {
  login: string | null = "";

  userData: userData = {
    role: "",
    status: "",
    rating: {
      place: 0,
      score: 0,
    },
    count: 0,
    digRub: 0,
    tokens: [{ uri: "", tokens: [] }],
    tasks: []
  };

  constructor() {
    makeAutoObservable(this);
  }

  getLogin() {
    this.login = localStorage.getItem("login");
  }

  async getRole() {
    let response = await $api.get(`/get_employee_role/${this.login}`);
    runInAction(() => {
      this.userData.role = response.data.role;
    });
  }

  async getStatus() {
    let response = await $api.get(`/get_employee_status/${this.login}`);
    runInAction(() => {
      this.userData.status = response.data.status;
    });
  }

  async getPR() {
    let response = await $api.get(`/get_personal_rating/${this.login}`);
    runInAction(() => {
      this.userData.rating = response.data;
    });
  }

  // async getPRID() {
  //   let response = await $api.get(
  //     `/get_personal_rating_in_department/${this.login}`
  //   );
  //   console.log(response.data);

  // }

  async getCOT() {
    let response = await $api.get(`/get_count_of_tasks/${this.login}`);
    runInAction(() => {
      this.userData.count = response.data.count;
    });
  }

  async getWB() {
    let response = await $api.get(`/get_wallet_balance/${this.login}`);
    runInAction(() => {
      this.userData.digRub = response.data.coinsAmount;
    });
  }

  async getNWB() {
    let response = await $api.get(`/get_wallet_nft_balance/${this.login}`);
    let tokens = response.data;
    if (tokens.length !== 0) {
      runInAction(() => {
        this.userData.tokens = tokens;
      });
    }
  }

  async getTasks() {
    let response = await $api.get(`/get_tasks/${this.login}`);
    runInAction(() => {
      this.userData.tasks = response.data
    });
  }
}
export default new Api();
