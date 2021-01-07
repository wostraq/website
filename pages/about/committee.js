import React from "react";
import Link from "next/link";
export default function Membership() {
  const names = {
    chair: "Yvonne Bramma",
    secretary: "Claire McCue",
    db_manager: "John Gardner",
    webmaster: "Daniel Silcock",
    traineecomms: "Gemma Scotland",
    conscomms: "Clare Currie",
  };
  return (
    <>
      <h2> Committee </h2>
      The organisation is led by a committee of its members:
      <h3> Chairperson </h3>
      {names.chair} <br />
      <a href="mailto:chair@wostraq.net">Contact</a>
      <br />
      Chairs committee meetings, steers development of the organisation,
      communicates with RAFT
      <h3> Secretary </h3>
      {names.secretary}
      <br />
      <a href="mailto:secretary@wostraq.net">Contact</a>
      <br />
      Records and distributes minutes for committee meetings, monitors WOSTRAQ
      email accounts.
      <h3>Database manager</h3>
      {names.db_manager} <br />
      <a href="mailto:db_manager@wostraq.net">Contact</a>
      <br />
      Obtain license for use of Redcap software and server to host the database,
      manage the database once set up
      <h3>IT Lead/Webmaster</h3>
      {names.webmaster} <br />
      <a href="mailto:webmaster@wostraq.net">Contact</a>
      <br />
      Set up and manage WOSTRAQ website and social media accounts
      <h3>Trainee communication lead</h3>
      {names.traineecomms}
      <br />
      <a href="mailto:traineecomms@wostraq.net">Contact</a>
      <br />
      Communication link between trainee members and the committee
      <h3>Consultant communication lead</h3>
      {names.conscomms}
      <br />
      <a href="mailto:conscomms@wostraq.net">Contact</a>
      <br />
      Communication link between consultants and the committee
    </>
  );
}
