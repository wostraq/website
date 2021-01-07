import React from "react";
import Link from "next/link";
export default function Membership() {
  return (
    <>
      <h2>Propose a project</h2>
      Any trainee WOSTRAQ member may submit a project proposal by completing the{" "}
      <a href="http://forms.wostraq.net/index.php/756755?lang=en">
        online form.
      </a>
      The committee will select proposals for distribution to the WOSTRAQ
      members for a vote to select which project to take forward.
      <br />
      Once a project proposal has been selected to be run by WOSTRAQ, the
      proposer will be designated the Regional Project Lead for that project
      unless he/she wishes to delegate this to someone else. The Regional
      Project Lead will be responsible for the overall running of the project,
      with the support of the committee.
      <br />
      It is the responsibility of the Regional Project Lead to present and/or
      publish the results of the project.
      <br />
      If they are unable to or do not wish to, they can delegate this task to a
      committee member or another WOSTRAQ member who has made a significant
      contribution to the project
      <br />
      Obtaining the correct approvals from the{" "}
      <a href="http://www.informationgovernance.scot.nhs.uk/pbpphsc/">
        {" "}
        Public Benefit and Privacy Panel
      </a>
      , ethics committee and local Caldicott Guardians are the responsibility of
      the Regional Project Lead.
      <h2>
        {" "}
        <a
          href="http://forms.wostraq.net/index.php/756755?lang=en"
          target="_blank"
        >
          Complete the online form here
        </a>
      </h2>
      For full details, including authorship rules, please refer to the{" "}
      <a href="/static/constitution.pdf"> WOSTRAQ constitution </a>
    </>
  );
}
