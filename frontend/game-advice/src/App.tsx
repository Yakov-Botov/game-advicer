import React, {useState} from 'react';
import View from '@vkontakte/vkui/dist/components/View/View';
import '@vkontakte/vkui/dist/vkui.css';

import {AppPanelsIds, RandomGamePanel} from './core/panels';

const App = () => {
	const [activePanel, setActivePanel] = useState<AppPanelsIds>(AppPanelsIds.RandomGame);

	return (
		<View activePanel={activePanel}>
			<RandomGamePanel/>
		</View>
	);
}

export default App;

