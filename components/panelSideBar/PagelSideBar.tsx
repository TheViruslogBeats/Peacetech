import styles from "./styles.module.scss";
import { BiWallet } from "react-icons/bi";
import { GiBackwardTime } from "react-icons/gi";
import { HiShoppingCart } from "react-icons/hi";
import { TbArrowsDoubleNeSw } from "react-icons/tb";

const PagelSideBar = () => {
  return (
    <div className={styles.sideBar}>
      <button className={styles.button + " " + styles.activeBTN}>
        <BiWallet />
      </button>
      <button className={styles.button}>
        <GiBackwardTime />
      </button>
      <button className={styles.button}>
        <HiShoppingCart />
      </button>
      <button className={styles.button}>
        <TbArrowsDoubleNeSw />
      </button>
    </div>
  );
};

export default PagelSideBar;
