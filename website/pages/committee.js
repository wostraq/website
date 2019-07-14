function CommitteeMember({person}){
  return (<div>
  <h3> {person.title} </h3> 
  <a href="#">{person.name}</a> <br>
  <a href={"mailto:"+person.email}>Contact</a><br>
  {person.role}
  </div>)}
  


function AboutCommittee(props){
  committeemembers=[
  {title:"Chairperson",name:"Yvonne Bramma",email:"chair@wostraq.net",role:"Chairs committee meetings, steers development of the organisation, communicates with RAFT"},
  {title:"Secretary",name:"Claire McCue",email:"secretary@wostraq.net",role:"Records and distributes minutes for committee meetings, monitors WOSTRAQ email accounts."},
  {title:"Database manager",name:"John Gardner",email:"db_manager@wostraq.net",role:"Obtain license for use of Redcap software and server to host the database, manage the database once set up"},
  {title:"IT Lead/Webmaster",name:"Daniel Silcock",email:"webmaster@wostraq.net",role:"Set up and manage WOSTRAQ website and social media accounts"},
  {title:"Trainee communication lead",name:"Gemma Scotland",email:"traineecomms@wostraq.net",role:"Communication link between trainee members and the committee"},
  {title:"Consultant communication lead",name:"Clare Currie",email:"conscomms@wostraq.net",role:"Communication link between consultants and the committee"}
  ]
    
  return (
    <div>
    <h2> Committee </h2>

    The organisation is led by a committee of its members:
    {committeemembers.map((member)=>(<CommitteeMember person={member}/>)}
    </div>)
}

export default AboutCommittee
