import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';

const BookImportScreen: React.FC = () => {
  const [profileUrl, setProfileUrl] = useState<string>('');

  const handleImport = () => {
    // TODO: Implement the import functionality
    console.log(`Importing books from: ${profileUrl}`);
  };

  return (
    <View>
      <Text>Import your GoodReads books</Text>
      <TextInput
        value={profileUrl}
        onChangeText={setProfileUrl}
        placeholder="Enter your GoodReads profile URL"
      />
      <Button title="Import" onPress={handleImport} />
    </View>
  );
};

export default BookImportScreen;
