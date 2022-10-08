import styles from "./styles.module.scss";
import { BiWallet } from "react-icons/bi";

const PagelSideBar = () => {
  return (
    <div className={styles.sideBar}>
      <button className={styles.button + " " + styles.activeBTN}>
        <BiWallet />
      </button>
      <button className={styles.button}>
        <BiWallet />
      </button>
      <button className={styles.button}>
        <BiWallet />
      </button>
      <button className={styles.button}>
        <BiWallet />
      </button>
    </div>
  );
};

export default PagelSideBar;
