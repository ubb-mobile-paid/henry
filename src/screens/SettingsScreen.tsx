import React from 'react';
import {Alert, ScrollView, StyleSheet, Text, View} from 'react-native';
import {NativeStackScreenProps} from '@react-navigation/native-stack';
import {RootStackParamList} from '../navigation/RootNavigator';
import SettingsRow from '../components/SettingsRow';

type Props = NativeStackScreenProps<RootStackParamList, 'Settings'>;

type Section = {
  title: string;
  rows: {label: string; onPress: () => void}[];
};

export default function SettingsScreen(_props: Props) {
  const sections: Section[] = [
    {
      title: 'Account',
      rows: [
        {label: 'Profile', onPress: () => Alert.alert('Profile')},
        {label: 'Sign Out', onPress: () => Alert.alert('Sign Out')},
      ],
    },
    {
      title: 'Notifications',
      rows: [
        {label: 'Push Notifications', onPress: () => Alert.alert('Push Notifications')},
        {label: 'Email Notifications', onPress: () => Alert.alert('Email Notifications')},
      ],
    },
    {
      title: 'Appearance',
      rows: [
        {label: 'Dark Mode', onPress: () => Alert.alert('Dark Mode')},
      ],
    },
    {
      title: 'About',
      rows: [
        {label: 'Privacy Policy', onPress: () => Alert.alert('Privacy Policy')},
        {label: 'Terms of Service', onPress: () => Alert.alert('Terms of Service')},
        {label: 'App Version', onPress: () => Alert.alert('Version', '1.0.0')},
      ],
    },
  ];

  return (
    <ScrollView style={styles.container} contentInsetAdjustmentBehavior="automatic">
      {sections.map(section => (
        <View key={section.title} style={styles.section}>
          <Text style={styles.sectionHeader}>{section.title.toUpperCase()}</Text>
          <View style={styles.sectionBody}>
            {section.rows.map(row => (
              <SettingsRow key={row.label} label={row.label} onPress={row.onPress} />
            ))}
          </View>
        </View>
      ))}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f2f2f7',
  },
  section: {
    marginTop: 24,
  },
  sectionHeader: {
    fontSize: 12,
    fontWeight: '600',
    color: '#6d6d72',
    marginBottom: 6,
    paddingHorizontal: 16,
    letterSpacing: 0.5,
  },
  sectionBody: {
    borderTopWidth: StyleSheet.hairlineWidth,
    borderTopColor: '#c6c6c8',
  },
});
