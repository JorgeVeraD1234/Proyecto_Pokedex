import 'react-native-gesture-handler';
import React from 'react';
import { StyleSheet, Text, View, Image, TextInput, Pressable } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { Register } from './registerView';
import { RecoverPassword } from "./recoverPasswordView"
import { EditUser } from "./editableView"

const Stack = createStackNavigator();

const Home = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <View>
        <Image
          source={{
            uri: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/2052px-Pok%C3%A9_Ball_icon.svg.png',
          }}
          style={{ width: 200, height: 200 }}
        />
      </View>
      <View>
        <Text style={styles.title}>Iniciar Sesión</Text>

        <Text style={styles.label}>Correo</Text>
        <TextInput style={styles.input} />

        <Text style={styles.label}>Contraseña</Text>
        <TextInput style={styles.input} secureTextEntry={true} />

        <Pressable style={styles.send}>
          <Text style={styles.textButton}>Enviar</Text>
        </Pressable>
      </View>
      <View style={styles.containerFooter}>
        <Pressable onPress={() => navigation.navigate('Register')}>
          <Text style={styles.footerText}>Regístrate</Text>
        </Pressable>

        <Pressable onPress={() => navigation.navigate('RecoverPassword')}>
          <Text style={styles.footerText}>RecoverPassword</Text>
        </Pressable>

        <Pressable onPress={() => navigation.navigate('EditUser')}>
          <Text style={styles.footerText}>EditUser</Text>
        </Pressable>
      </View>
    </View>
  );
};

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={Home} options={{ title: 'Inicio' }} />
        <Stack.Screen name="Register" component={Register} options={{ title: 'Registro' }} />
        <Stack.Screen name="RecoverPassword" component={RecoverPassword} options={{ title: 'RecoverPassword' }} />
        <Stack.Screen name="EditUser" component={EditUser} options={{ title: 'EditUser' }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
    padding: 20,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
  },
  label: {
    fontSize: 15,
    marginTop: 10,
  },
  input: {
    borderRadius: 8,
    borderWidth: 1,
    fontSize: 15,
    padding: 10,
    marginTop: 5,
  },
  send: {
    backgroundColor: 'black',
    borderRadius: 10,
    marginTop: 15,
    alignItems: 'center',
  },
  textButton: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 15,
  },
  containerFooter: {
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 20,
  },
  footerText: {
    fontSize: 12,
    margin: 5,
    color: 'black',
  },
});
