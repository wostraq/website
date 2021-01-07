import React from "react";
import { useRouter } from "next/router";
import Link from "next/link";
import Head from "next/head";

function NavMenu({ parentMenu = "root", endpointPrefix, text, children }) {
  const router = useRouter();
  return (
    <li
      className={router.asPath.startsWith(endpointPrefix) ? styles.active : ""}
    >
      <input
        id={endpointPrefix}
        className={styles.navMenuInput}
        type="radio"
        name={parentMenu}
      />
      <label class={styles.navmenuitem} htmlFor={endpointPrefix}>
        {text}
      </label>
      <ul class={styles.collapsible}>{children}</ul>
    </li>
  );
}
function NavItem({ endpoint, text }) {
  const router = useRouter();
  console.log(router.asPath);
  return (
    <li className={router.asPath == endpoint ? styles.active : ""}>
      <Link href={endpoint}>
        <a className={styles.navmenuitem}>{text}</a>
      </Link>
    </li>
  );
}

import styles from "../styles/sidebar.module.css";
import "../styles/style.css";

export default function App({ Component, pageProps }) {
  const [isOpen, setOpen] = React.useState(false);
  React.useEffect(() => setOpen(false), [useRouter().asPath]);
  return (
    <>
      <Head>
        <meta charSet="utf-8" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta
          name="description"
          content="WOSTRAQ - West of Scotland Trainees Research, Audit and QI network"
        />
        <meta name="author" content="WOSTRAQ" />
        <link rel="shortcut icon" href="/static/favicon.ico" />
        <title>WOSTRAQ</title>

        <link
          href="https://fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic,700italic"
          rel="stylesheet"
          type="text/css"
        />
      </Head>

      <div className={styles.wrapper} onClick={() => setOpen(false)}>
        <nav
          className={`${styles.sidebar} ${isOpen ? styles.active : ""}`}
          onClick={(e) => e.stopPropagation()}
        >
          <div className={styles.sidebarHeader}>
            <h3>
              <Link href="/">
                <a>
                  <img
                    class="img-responsive d-block"
                    src="/img/wostraqlogo.png"
                  />
                </a>
              </Link>
            </h3>
          </div>
          <ul>
            <NavMenu endpointPrefix="/about" text="About">
              <NavItem endpoint="/about/membership" text="Membership" />
              <NavItem endpoint="/about/local" text="Local Leads" />
              <NavItem endpoint="/about/committee" text="Committee" />
              <NavItem
                endpoint="/about/curriculum"
                text="RCoA CCT curriculum"
              />
            </NavMenu>
            <NavMenu endpointPrefix="/projects" text="Projects">
              <NavItem endpoint="/projects/current" text="Current Projects" />
              <NavItem endpoint="/projects/previous" text="Previous Projects" />
              <NavItem endpoint="/projects/propose" text="Propose a project" />
              <NavItem
                endpoint="/projects/proposals"
                text="Proposed projects"
              />
            </NavMenu>
          </ul>
          <ul class="list-unstyled CTAs">
            <li>
              <a
                href="http://www.example.com"
                class="download"
                target="dataentry"
              >
                Access the data entry form
                <i class="glyphicon glyphicon-lock"></i>
              </a>
            </li>
            <li>
              <Link href="/join">
                <a class="download" target="join">
                  Join WoSTRAQ
                </a>
              </Link>
            </li>
            <li>
              <Link href="/membersarea">
                <a class="download" target="membersarea">
                  Access the members area
                  <i class="glyphicon glyphicon-lock"></i>
                </a>
              </Link>
            </li>
          </ul>
          <div className={styles.backinbox}>.</div>
        </nav>

        <div id="content" class="flaskbb-layout">
          <div className={styles.topnav}>
            <div>
              <button
                type="button"
                id="sidebarCollapse"
                class="btn btn-info
                navbar-btn"
                onClick={(e) => {
                  e.stopPropagation();
                  setOpen((s) => !s);
                }}
              >
                <svg
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  x="0px"
                  y="0px"
                  width="24px"
                  height="24px"
                  viewBox="0 0 24 24"
                  style={{ ["enable-background"]: "new 0 0 24 24" }}
                >
                  <g id="Icons" style={{ opacity: 0.75 }}>
                    <path
                      id="menu"
                      d="M6,15h12c0.553,0,1,0.447,1,1v1c0,0.553-0.447,1-1,1H6c-0.553,0-1-0.447-1-1v-1C5,15.447,5.447,15,6,15z M5,11v1
		c0,0.553,0.447,1,1,1h12c0.553,0,1-0.447,1-1v-1c0-0.553-0.447-1-1-1H6C5.447,10,5,10.447,5,11z M5,6v1c0,0.553,0.447,1,1,1h12
		c0.553,0,1-0.447,1-1V6c0-0.553-0.447-1-1-1H6C5.447,5,5,5.447,5,6z"
                    />
                  </g>
                  <g id="Guides" style={{ display: "none" }}></g>
                </svg>
              </button>
            </div>
            <div className={styles.titlebar}>
              <Link href="/">
                <a>
                  <img
                    style={{ height: "3em" }}
                    src="/img/wostraqlogo.png"
                    title="WoSTRAQ"
                  />
                </a>
              </Link>
            </div>
          </div>
          <Component {...pageProps} />
        </div>
      </div>
    </>
  );
}
