import React, { Component,useState } from 'react'

import { Button, Responsive,Header, Icon, Image, Menu, Segment, Sidebar } from 'semantic-ui-react'


import Router from 'next/router'
import Link from 'next/link'
import App, { Container } from 'next/app';


function Menubar(props){

  [isVisible,setVisible]=useState(true)
  [width,setWidth]=useState(0)

  const handleHideClick = () => setVisible(false)
  const handleShowClick = () => setVisible(true)
  const handleSidebarHide = () => setVisible(false)
  const handleOnUpdate = (e, { width }) => setWidth(width)
  const sidebardirection = width >= Responsive.onlyComputer.minWidth ? 'left' : 'top'

  return (
      <div>
      <Responsive fireOnMount onUpdate={handleOnUpdate}/>
      <Button.Group>
          <Button disabled={visible} onClick={handleShowClick}>
            Show sidebar
          </Button>
          <Button disabled={!visible} onClick={handleHideClick}>
            Hide sidebar
          </Button>
        </Button.Group>

        <Sidebar.Pushable as={Segment}>
          <Sidebar
            as={Menu}
            animation='push'
            icon='labeled'
            inverted
            onHide={handleSidebarHide}
            vertical
            direction={sidebardirection}
            visible={visible}
            width='thin'
          >

	     {props.children}
          </Sidebar>


          <Sidebar.Pusher>
            <Segment basic>
              {props.content}
            </Segment>
          </Sidebar.Pusher>
        </Sidebar.Pushable>
      </div>
    )
  }


function NavMenu({children=null,prefix,pagename}){
  const active=(Router.pathname.indexOf(prefix)>=0)
  return(
    <Menu.Item as='a'  active={active}>
      {pagename}
      {active?<Menu>children</Menu>:null}
    </Menu.Item>
  )
}

function NavItem({href,pagename}){
  const active=(Router.pathname.indexOf(href)>=0)
  return(
    <Menu.Item as={Link}
     active={active}
     href={href}>
      <a>{pagename}</a>    
    </Menu.Item>
  )
}


class MyApp extends App {
  static async getInitialProps({ Component, ctx }) {
    let pageProps = {};

    if (Component.getInitialProps) {
      pageProps = await Component.getInitialProps(ctx);
    }

    return { pageProps };
  }

  render() {
    const { Component, pageProps } = this.props;

    return (
      <Container>
        <Menubar content={<Component {...pageProps} />}>
          <NavMenu prefix='content.about' pagename='About'>
            <NavItem href='about/membership' pagename='Membership'/>
            <NavItem href='about/local' pagename='Local leads'/>
            <NavItem href='about/committee' pagename='Committee'/>
          </NavMenu>
          <NavMenu prefix='projects' pagename="Projects'>
            <NavItem href='projects/previous' pagename='Previous projects'/>
            <NavItem href='projects/propose' pagename='Propose a project'/>
            <NavItem href='projects/proposals' pagename="Proposed projects'/>
          </NavMenu>
          <NavMenu prefix='members' pagename="Members">
            <NavItem href='members/join' pagename="Join us"/>
            <NavItem href='members/mydetails' pagename='My details'
          </NavMenu>
        </Menubar>
      </Container>
    );
  }
}

export default MyApp;
