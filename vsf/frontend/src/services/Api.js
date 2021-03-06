import { notification } from 'antd';

export const getSchedules = (search) => fetch(`/api/schedule/?search=${search}`);
export const getStats = () => fetch('/api/stats/');
export const getLastSpreadsheetsProcessed = () => fetch('api/spreadsheet/?limit=3&processed=true&ordering=-date');
export const postEmailNotification = (values) =>
  fetch('/api/notification/', {
    method: 'POST', // or 'PUT'
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(values),
  });

export const saveEmailNotification = async (values) => {
  try {
    values.birth_date = values.birth_date.format('YYYY-MM-DD');
    const response = await postEmailNotification(values);
    if (response.ok) {
      notification.success({
        message: 'Massa!',
        description:
          'Assim que a gente ver seu nome na lista divulgada pela prefeitura vamos te mandar um email com os dados =)',
        duration: 10,
      });
      return;
    }
    const data = await response.json();
    if (data.non_field_errors[0].includes('must make a unique set')) {
      notification.info({
        message: 'Já foi oh ^^',
        description: 'Perainda... esse email e nome já foi cadastrado, é só esperar!',
        duration: 10,
      });
      return;
    }
  } catch (error) {
    console.error('Error:', error);
  }

  notification.error({
    message: 'Eita mah, não rolou =/',
    description:
      'Tivemos um probleminha para cadastrar a notificação, rola tentar de novo mais tarde?',
    duration: 10,
  });
};
