import React from 'react';
import { View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

// Placeholder components
const BookImportScreen = () => <View><Text>Book Import Screen</Text></View>;
const ProfileDetailScreen = () => <View><Text>Profile Detail Screen</Text></View>;
const RecommendationCreateScreen = () => <View><Text>Recommendation Create Screen</Text></View>;

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="BookImport">
        <Stack.Screen name="BookImport" component={BookImportScreen} options={{ title: 'Import Books' }} />
        <Stack.Screen name="ProfileDetail" component={ProfileDetailScreen} options={{ title: 'Profile' }} />
        <Stack.Screen name="RecommendationCreate" component={RecommendationCreateScreen} options={{ title: 'Recommendations' }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
