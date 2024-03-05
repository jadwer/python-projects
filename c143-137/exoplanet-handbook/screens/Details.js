import React, { Component } from "react";
import {
  View,
  Text,
  StyleSheet,
  Alert,
  Image,
  ImageBackground,
} from "react-native";
import axios from "axios";

export default class DetailsScreen extends Component {
  constructor(props) {
    super(props);
    this.state = {
      details: {},
      imagePath: "",
      url: `https://4aeb-2806-2f0-92c0-c3d0-a1fd-1263-dcde-adcb.ngrok-free.app/planet?name=${this.props.navigation.getParam(
        "planet_name"
      )}`,
    };
  }

  componentDidMount() {
    this.getDetails();
  }
  getDetails = () => {
    const { url } = this.state;
    axios
      .get(url)
      .then((response) => {
        this.setDetails(response.data.data);
      })
      .catch((error) => {
        Alert.alert(error.message);
      });
  };

  setDetails = (planetDetails) => {
    const planetType = planetDetails.planet_type;
    let imagePath = "";
    switch (planetType) {
      case "Gas Giant":
        imagePath = require("../assets/Gas_Giant.png");
        break;
      case "Terrestrial":
        imagePath = require("../assets/Terrestrial.png");
        break;
      case "Super Earth":
        imagePath = require("../assets/Super_Earth.png");
        break;
      case "Neptune Like":
        imagePath = require("../assets/Neptune-like.png");
        break;
      default:
        imagePath = require("../assets/Gas_Giant.png");
    }

    this.setState({
      details: planetDetails,
      imagePath: imagePath,
    });
  };

  render() {
    const { details, imagePath } = this.state;
    if (details.specifications) {
      return (
        <View style={styles.container}>
          <ImageBackground
            source={require("../assets/bg.png")}
            style={{ flex: 1, paddingTop: 20 }}
          >
            <Image
              source={imagePath}
              style={{
                height: 250,
                width: 250,
                marginTop: 50,
                alignSelf: "center",
              }}
            />
            <View style={{ marginTop: 0 }}>
              <Text style={styles.planetName}>{details.name}</Text>
              <View style={{ alignSelf: "center" }}>
                <Text
                  style={styles.planetData}
                >{`Distancia a la tierra: ${details.distance_from_earth}`}</Text>
                <Text
                  style={styles.planetData}
                >{`Distancia al sol: ${details.distance_from_their_sun}`}</Text>
                <Text
                  style={styles.planetData}
                >{`Gravedad: ${details.gravity}`}</Text>
                <Text
                  style={styles.planetData}
                >{`Período orbital: ${details.orbital_period}`}</Text>
                <Text
                  style={styles.planetData}
                >{`Velocidad orbital: ${details.orbital_speed.toFixed(8)}`}</Text>
                <Text
                  style={styles.planetData}
                >{`Masa del planeta: ${details.planet_mass}`}</Text>
                <Text
                  style={styles.planetData}
                >{`Radio del planeta: ${details.planet_radius}`}</Text>
                <Text
                  style={styles.planetData}
                >{`Tipo de planeta: ${details.planet_type}`}</Text>
                <View style={{ flexDirection: "row",alignSelf:"center" }}>
                  <Text style={styles.planetData}>
                    {details.specifications ? `Especificaciones: ` : ""}
                  </Text>
                  {details.specifications.map((item, index) => (
                    <Text key={index.toString()} style={styles.planetData}>
                      {item}&nbsp;
                    </Text>
                  ))}
                </View>
              </View>
            </View>
          </ImageBackground>
        </View>
      );
    }
    return null;
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  planetName: {
    fontSize: 25,
    color: "white",
    fontWeight: "bold",
    textAlign: "center",
    marginBottom: 20,
    width: "80%",
    alignSelf: "center",
    fontFamily:"monospace"
  },
  planetData: {
    fontSize: 15,
    color: "white",
    textAlign:"center",
    fontFamily:"monospace"
  },
});