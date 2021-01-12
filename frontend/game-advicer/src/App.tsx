import './App.css'
import React, { useCallback, useState } from 'react'
import '@vkontakte/vkui/dist/vkui.css'

import {
    AppPanelsIds,
    FavoriteListPanel,
    ProfilePanel,
    RandomGamePanel,
} from './core/panels'
import { ConfigProvider, Epic, Tabbar, TabbarItem, View } from '@vkontakte/vkui'
import { IconsAdapter } from './shared/components'

export const App = React.memo(() => {
    const [activeStory, setActiveStory] = useState<AppPanelsIds>(
        AppPanelsIds.RandomGame
    )

    const handleChangeActiveStory = useCallback(
        (e: React.MouseEvent<HTMLElement>) => {
            if (!e?.currentTarget?.dataset?.story) return

            const story = e.currentTarget.dataset.story
            setActiveStory(story as AppPanelsIds)
        },
        []
    )

    /** TODO: реализовать переключение темы по кнопке */
    /** TODO: реализовать вывод уведомлений (ошибки, предупреждения) */

    return (
            <ConfigProvider scheme="space_gray">
                <Epic
                    activeStory={activeStory}
                    tabbar={
                        <Tabbar>
                            <TabbarItem
                                onClick={handleChangeActiveStory}
                                selected={
                                    activeStory === AppPanelsIds.FavoriteList
                                }
                                data-story={AppPanelsIds.FavoriteList}
                                text="Понравившиеся"
                            >
                                <IconsAdapter iconType={'IconLikeOutline'} />
                            </TabbarItem>
                            <TabbarItem
                                onClick={handleChangeActiveStory}
                                selected={
                                    activeStory === AppPanelsIds.RandomGame
                                }
                                data-story={AppPanelsIds.RandomGame}
                                text="Случайная игра"
                            >
                                <IconsAdapter iconType={'IconGameOutline'} />
                            </TabbarItem>
                            <TabbarItem
                                onClick={handleChangeActiveStory}
                                selected={activeStory === AppPanelsIds.Profile}
                                data-story={AppPanelsIds.Profile}
                                text="Профиль"
                            >
                                <IconsAdapter
                                    iconType={'IconUserCircleOutline'}
                                />
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
                    <View
                        id={AppPanelsIds.Profile}
                        activePanel={AppPanelsIds.Profile}
                    >
                        <ProfilePanel id={AppPanelsIds.Profile} />
                    </View>
                </Epic>
            </ConfigProvider>
    )
})
