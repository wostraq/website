import React from "react";
import Link from "next/link";
export default function Membership() {
  return (
    <>
      <h2> Membership </h2>
      Membership of WOSTRAQ is open to any registered anaesthetic trainee within
      the West of Scotland School of Anaesthesia. Consultants, doctors outwith
      anaesthetic training, medical students and other healthcare professionals
      may become associate members of WOSTRAQ.Their role will usually be limited
      to local involvement in projects. Any member of WOSTRAQ may submit QI
      proposals for support by WOSTRAQ.
      <br />
      To join WOSTRAQ, please complete the{" "}
      <Link href="/joinus">
        <a> online registration form. </a>
      </Link>
      Membership applications will be vetted by the committee before approval.
      <br />
      <hr />
      For full details please refer to the{" "}
      <a href="/assets/constitution.pdf"> WOSTRAQ constitution</a>
    </>
  );
}
