import React from "react";
import Link from "next/link";
export default function Local() {
  return (
    <>
      <h2>Local links</h2>
      To contact your local link person, please see the list below
      <h3> Greater Glasgow and Clyde </h3>
      <ul>
        <li>
          {" "}
          Glasgow Royal Infirmary/Stobhill : <a href="#"> TBC </a>{" "}
        </li>
        <li>
          {" "}
          Queen Elizabeth University Hospital/Gartnavel/Victoria Hospital:{" "}
          <a href="#"> TBC </a>
        </li>
        <li>
          {" "}
          Royal Alexandra Hospital/Inverclyde Royal Hospital/Vale of Leven
          Hospital: <a href="#"> TBC </a>
        </li>
      </ul>
      <h3> Lanarkshire </h3>
      <ul>
        <li>
          {" "}
          Monklands : <a href="#"> TBC </a>{" "}
        </li>
        <li>
          {" "}
          Hairmyres: <a href="#"> TBC </a>
        </li>
        <li>
          {" "}
          Wishaw: <a href="#"> TBC </a>
        </li>
      </ul>
      <h3> Ayrshire and Arran </h3>
      <ul>
        <li>
          {" "}
          Crosshouse : <a href="#"> TBC </a>{" "}
        </li>
        <li>
          {" "}
          Ayr: <a href="#"> TBC </a>
        </li>
      </ul>
      <h3> Dumfries and Galloway </h3>
      <ul>
        <li>
          {" "}
          Dumfries and Galloway Royal Infirmary : <a href="#"> TBC </a>{" "}
        </li>
      </ul>
      <h3> Forth Valley </h3>
      <ul>
        <li>
          {" "}
          Forth Valley Royal Infirmary : <a href="#"> TBC </a>{" "}
        </li>
      </ul>
    </>
  );
}
