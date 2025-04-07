import { StyleSheet, Text, View, TextInput, Pressable } from 'react-native';
import { useState } from 'react';




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
        color: 'black',
        marginBottom: 20,
    },
    label: {
        fontSize: 15,
        color: 'black',
        marginTop: 15,
    },
    input: {
        borderRadius: 8,
        borderWidth: 1,
        fontSize: 15,
        padding: 12,
        marginTop: 8,
        backgroundColor: 'white'
    },
    send: {
        backgroundColor: 'black',
        borderRadius: 8,
        marginTop: 20,
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
        marginTop: 30,
    },
    footerText: {
        fontSize: 12,
        margin: 5,
        color: 'black',
    },
});







export const Register = () => {

    const [data, setData] = useState({
        name: "",
        email: "",
        password: "",
        cPassword: ""
    })

    const onChange = (field, value) => {
        setData({ ...data, [field]: value })
    }

    const onSubmit = async () => {
        try {
            console.log("Exito")
        } catch (error) {
            console.error("Fallo: ", error)
        }
    }


    return (

        <View style={styles.container}>

            <Text style={styles.title}> Registrarse </Text>

            <View>

                <Text style={styles.label}>Nombre completo</Text>
                <TextInput
                    style={styles.input}
                    value={data.name}
                    onChangeText={
                        (value) => onChange('name', value)}
                />

                <Text style={styles.label}>Correo</Text>
                <TextInput
                    style={styles.input}
                    value={data.email}
                    onChangeText={
                        (value) => onChange("email", value)

                    }
                />

                <Text style={styles.label}>Contraseña</Text>
                <TextInput
                    style={styles.input}
                    value={data.password}
                    secureTextEntry={true}
                    onChangeText={
                        (value) => onChange("password", value)
                    }
                />

                <Text style={styles.label}>Confirmar contraseña</Text>
                <TextInput
                    style={styles.input}
                    value={data.cPassword}
                    secureTextEntry={true}
                    onChangeText={
                        (value) => onChange("cPassword", value)
                    }
                />


                <Pressable style={styles.send} onPress={onSubmit}>
                    <Text style={styles.textButton}>
                        Enviar
                    </Text>
                </Pressable>


            </View>
        </View>
    );
}
