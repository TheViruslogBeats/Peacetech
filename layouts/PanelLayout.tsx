import Head from "next/head";
import React from "react";
import PanelTopBar from "../components/panelTopBar/PanelTopBar";
import styles from "./styles.module.scss";
import PanelSideBar from "../components/panelSideBar/PagelSideBar";

interface LayoutProps {
  children: React.ReactNode;
}

const PanelLayout = ({ children }: LayoutProps) => {
  return (
    <>
      <Head>
        <title>ВТБ | Платформа</title>
        <link rel="icon" href="/favico/favicon.ico" />
      </Head>
      <div className={styles.mainCnt}>
        <PanelTopBar />
        <div className={styles.container}>
          <PanelSideBar />
          {children}
        </div>
      </div>
    </>
  );
};

export default PanelLayout;
