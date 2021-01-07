import React from "react";
import Link from "next/link";
export default function Membership({ nameslist = [] }) {
  return (
    <>
      <h2>Current projects</h2>
      <h3>Post-operative nausea and vomiting</h3>
      Our first project began in January 2018 and looks at postoperative nausea
      and vomiting in the West of Scotland.
      <br />
      This project also gave us an opportunity to test the network.
      <br />
      Over the region, we collected data on over 300 patients. This would not
      have been possible without the help of our regional data collectors:
      <br />
      <br />
      {nameslist.map((n) => <a title={n[1]}>{n[0]}</a>).join(",")}
      <hr />
      For more information on this project please{" "}
      <a href="/assets/ponv/factsheet.pdf">read the factsheet</a>
      More information will follow when we have analysed the results of this
      project
    </>
  );
}
