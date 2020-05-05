import React from "react";
import { Col, Row, Card, CardBody, CardText, CardImg, CardDeck, Button } from "reactstrap";
import { Link } from "react-router-dom";
import { useAuth0 } from "../react-auth0-spa";
import "../App.css";
// import ActorsImg from '../assets/actors.jpg'
// import MoviesImg from '../assets/movies.jpg'

export const Home = () => {
  const { isAuthenticated } = useAuth0();
  return (
    <>
      {isAuthenticated ? (
        <CardDeck>
          <Card className="homepage">
            <CardImg
              top
              width="100%"
              height="70%"
              // src="https://image.shutterstock.com/image-photo/movie-clapper-film-reel-on-600w-169841813.jpg"
              src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQJYRa6_-OqbNgGPogzlkAvuQqTA3mI-MMKbTFDQcgPOJtrDFoc&usqp=CAU"
              alt="Movies img"
            />
            <CardBody>
              <Link to="/movies"><div className="text-center"><Button outline color="info">Manage movies</Button></div></Link>
            </CardBody>
          </Card>
          <Card className="homepage">
            <CardImg
              top
              width="100%"
              height="70%"
              // src="https://image.shutterstock.com/image-photo/medium-shot-actors-rehearsing-theater-600w-1270982080.jpg"
              src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRnnXQDMqx2vmQf1TcjDB9OKcWqLSnFxffoMDpV5di6AOaNlfaK&usqp=CAU"
              alt="Actors img"
            />
            <CardBody>
              <Link to="/actors-details"><div className="text-center"><Button outline color="info">Manage actors</Button></div></Link>
            </CardBody>
          </Card>
        </CardDeck>
      ) : (
          <Card className="homepage">
            <CardBody>
              <CardText>
              This platform models a company that is responsible for creating movies, managing 
              and assigning actors to those movies. You can login as the following:
              </CardText>
              <CardText>
              <strong>Casting assistant</strong> -  Authorized to see the details of the movies and the actors.
              <p>
               <ul>
                  <li>Username: <strong>castassistant@gmail.com</strong></li>
                 <li>password: <strong>passworD1$</strong></li>
               </ul>
              </p>
              </CardText>
              <CardText>
              <strong>Casting Director</strong> - Have all the priviledges of a Casting Assistant and authorized to create new Actors and edit the details of Movies
              <p>
                <ul>
                  <li>Username: <strong>castdirector@gmail.com</strong></li>
                  <li>password: <strong>passwordD2$</strong></li>
                </ul>
              </p>
              </CardText>
              <CardText>
              <strong>Executive Producer</strong> - Have all the priviledges of a Casting Director and authorized to edit Actors, create and delete Movies.
              <p>
                <ul>
                  <li>Username: <strong>castproducer@gmail.com</strong></li>
                  <li>password: <strong>passworD3$</strong></li>
                </ul>
              </p>
              </CardText>
              <CardText>
              Otherwise, you can register and login using your own account. Make use of your google, facebook or lindkedIn to login.
              You will have limited access in using the platform though unless given desired permissions.
              </CardText>
            </CardBody>
          </Card>
      )}
    </>
  );
};