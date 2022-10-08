import styles from "./styles.module.scss";
import { GiHamburgerMenu } from "react-icons/gi";
import { BiSearchAlt } from "react-icons/bi";
import { TbMessageCircle } from "react-icons/tb";
import NotificationsModal from "./components/NotificationsModal";
import panelPage from "../../states/panelPage";

const PanelTopBar = () => {
  return (
    <div className={styles.panelTopBar}>
      <div className={styles.panelSideBarButton}>
        <button>
          <GiHamburgerMenu />
        </button>
      </div>
      <div className={styles.userInfo}>
        <div className={styles.topBarSearch}>
          <input type="text" />
          <BiSearchAlt />
        </div>
        <div className={styles.userInfoContainer}>
          <div
            onClick={() => {
              panelPage.setNM(true);
            }}
          >
            <TbMessageCircle />
            <p>100</p>
          </div>
          <h3>Шматов Егор Сергеевич</h3>
          <img
            src="https://cdn.discordapp.com/attachments/934798571688054914/1024374884819808357/691235880.jpeg"
            alt="usr"
          />
        </div>
      </div>
      <NotificationsModal />
    </div>
  );
};

export default PanelTopBar;
