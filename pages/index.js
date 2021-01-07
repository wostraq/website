import Head from "next/head";
import styles from "../styles/Home.module.css";

export default function Home() {
  return (
    <div>
      <h2> Welcome to WOSTRAQ </h2>
      WOSTRAQ are a group of anaesthetists in training, set up in order to
      facilitate collaborative, multi-centre audit and research in anaesthesia
      within the NHS hospitals in the West of Scotland. We aim:
      <ul>
        <li>
          To establish a regional network of anaesthetic trainees to conduct
          multi-centre research, audit and quality improvement{" "}
        </li>
        <li>
          To improve the quality and impact of audit and quality improvement
          projects in the West of Scotland.{" "}
        </li>
        <li>
          To allow trainees to continue their involvement in research and audit
          projects as they migrate around the deanery.{" "}
        </li>
        <li>
          To build partnerships between anaesthetic departments in the West of
          Scotland, with the overall aim of working together towards improving
          the quality of patient care.{" "}
        </li>
        <li>
          To participate in national audit and research projects and to attract
          national funding for research and audit work.{" "}
        </li>
      </ul>
      <hr />
      For more information please{" "}
      <a href="mailto:committee@wostraq.net">contact the committee</a> or read
      the <a href="/assets/constitution.pdf"> WoSTRAQ Constitution </a>
      <hr />
    </div>
  );
}
