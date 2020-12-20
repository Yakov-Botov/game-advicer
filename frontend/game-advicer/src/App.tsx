import React, { useState } from 'react'
import '@vkontakte/vkui/dist/vkui.css'

import { AppPanelsIds, RandomGamePanel } from './core/panels'
import { FavoriteListPanel } from './core/panels/FavoriteListPanel'
import { Tabbar, Epic, View, TabbarItem } from '@vkontakte/vkui'
import { IconsAdapter } from './shared/components'

const App = () => {
    const [activeStory, setActiveStory] = useState<AppPanelsIds>(
        AppPanelsIds.RandomGame
    )

    const handleChangeActiveStory = () => {}

    return (
        <Epic
            activeStory={activeStory}
            tabbar={
                <Tabbar>
                    <TabbarItem
                        onClick={handleChangeActiveStory}
                        selected={activeStory === AppPanelsIds.FavoriteList}
                        data-story={AppPanelsIds.FavoriteList}
                        text="Понравившиеся"
                    >
                        <IconsAdapter iconType={'Icon28LikeOutline'} />
                    </TabbarItem>
                    <TabbarItem
                        onClick={handleChangeActiveStory}
                        selected={activeStory === AppPanelsIds.RandomGame}
                        data-story={AppPanelsIds.RandomGame}
                        text="Случайная игра"
                    >
                        <IconsAdapter iconType={'Icon28GameOutline'} />
                    </TabbarItem>
                    <TabbarItem
                        onClick={handleChangeActiveStory}
                        selected={activeStory === AppPanelsIds.Profile}
                        data-story={AppPanelsIds.Profile}
                        text="Профиль"
                    >
                        <IconsAdapter iconType={'Icon28UserCircleOutline'} />
                    </TabbarItem>
                </Tabbar>
            }
        >
            <View
                id={AppPanelsIds.FavoriteList}
                activePanel={AppPanelsIds.FavoriteList}
            >
                <FavoriteListPanel id={AppPanelsIds.FavoriteList} />
            </View>
            <View
                id={AppPanelsIds.RandomGame}
                activePanel={AppPanelsIds.RandomGame}
            >
                <RandomGamePanel id={AppPanelsIds.RandomGame} />
            </View>
        </Epic>
    )
}

export default App
