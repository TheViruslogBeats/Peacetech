import { motion } from "framer-motion";
import { observer } from "mobx-react-lite";
import styles from "./styles.module.scss";
import panelPage from "../../../states/panelPage";

const NotificationsModal = () => {
  return (
    <>
      <motion.div
        className={styles.blackBox}
        initial={{ width: 0, height: 0, opacity: 0 }}
        animate={{
          width: panelPage.notifications ? "100%" : 0,
          height: panelPage.notifications ? "100%" : 0,
        }}
        transition={{ duration: 1, type: "spring" }}
        onClick={() => {
          panelPage.setNM(false);
        }}
      ></motion.div>
      <motion.div
        className={styles.notificationModal}
        initial={{ transform: "translate(-50%, -165%)", opacity: 0 }}
        animate={{
          transform: panelPage.notifications
            ? "translate(-50%, -50%)"
            : "translate(-50%, -165%)",
          opacity: 1,
        }}
        transition={{ duration: 0.75 }}
      >
        <div className={styles.notifications}>
          <div className={styles.notification}>
            <img
              src="https://sun1-88.userapi.com/impg/Tbm0VBe6G7T-7nzMXUbm2FZU1rX-t7hGuf8exA/8EQ1Ot-IKjw.jpg?size=965x1240&quality=96&sign=e317b7a4fbec9f97879b184bca460e01&type=album"
              alt=""
            />

            <div>
              <p>
                У вас непрочитанное сообщение от <b>Николая Никифорова</b>
              </p>
            </div>
          </div>
          <div className={styles.notification}>
            <img
              src="https://sun1-88.userapi.com/impg/Tbm0VBe6G7T-7nzMXUbm2FZU1rX-t7hGuf8exA/8EQ1Ot-IKjw.jpg?size=965x1240&quality=96&sign=e317b7a4fbec9f97879b184bca460e01&type=album"
              alt=""
            />

            <div>
              <p>
                У вас непрочитанное сообщение от <b>Николая Никифорова</b>
              </p>
            </div>
          </div>
          <div className={styles.notification}>
            <img
              src="https://sun1-88.userapi.com/impg/Tbm0VBe6G7T-7nzMXUbm2FZU1rX-t7hGuf8exA/8EQ1Ot-IKjw.jpg?size=965x1240&quality=96&sign=e317b7a4fbec9f97879b184bca460e01&type=album"
              alt=""
            />

            <div>
              <p>
                У вас непрочитанное сообщение от <b>Николая Никифорова</b>
              </p>
            </div>
          </div>
          <div className={styles.notification}>
            <img
              src="https://sun1-88.userapi.com/impg/Tbm0VBe6G7T-7nzMXUbm2FZU1rX-t7hGuf8exA/8EQ1Ot-IKjw.jpg?size=965x1240&quality=96&sign=e317b7a4fbec9f97879b184bca460e01&type=album"
              alt=""
            />

            <div>
              <p>
                У вас непрочитанное сообщение от <b>Николая Никифорова</b>
              </p>
            </div>
          </div>
          <div className={styles.notification}>
            <img
              src="https://sun1-88.userapi.com/impg/Tbm0VBe6G7T-7nzMXUbm2FZU1rX-t7hGuf8exA/8EQ1Ot-IKjw.jpg?size=965x1240&quality=96&sign=e317b7a4fbec9f97879b184bca460e01&type=album"
              alt=""
            />

            <div>
              <p>
                У вас непрочитанное сообщение от <b>Николая Никифорова</b>
              </p>
            </div>
          </div>
          <div className={styles.notification}>
            <img
              src="https://sun1-88.userapi.com/impg/Tbm0VBe6G7T-7nzMXUbm2FZU1rX-t7hGuf8exA/8EQ1Ot-IKjw.jpg?size=965x1240&quality=96&sign=e317b7a4fbec9f97879b184bca460e01&type=album"
              alt=""
            />

            <div>
              <p>
                У вас непрочитанное сообщение от <b>Николая Никифорова</b>
              </p>
            </div>
          </div>
        </div>
        <button>Мессенджер</button>
      </motion.div>
    </>
  );
};

export default observer(NotificationsModal);
